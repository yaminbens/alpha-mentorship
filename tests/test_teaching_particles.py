from pathlib import Path
import importlib.util
import numpy as np
import nbformat

R=Path(__file__).resolve().parent.parent
spec=importlib.util.spec_from_file_location('teaching_particles',R/'simulation/teaching_particles.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

def test_closed_partition_and_reproducible_opening():
    closed=m.mixing_run(0);opened=m.mixing_run(1)
    np.testing.assert_array_equal(closed['positions'][0],opened['positions'][0])
    assert (closed['measure']==0).all()
    assert opened['measure'][50] >= 1/3
    assert np.isfinite(opened['positions']).all()
    assert ((opened['positions']>=0)&(opened['positions']<=1)).all()
    np.testing.assert_array_equal(opened['positions'],m.mixing_run(1)['positions'])

def test_reflection_matches_unfolded_motion():
    x,v=m.reflect_coordinate(np.array([.99,.01,.2]),np.array([1.,-1.,3.]),.7)
    np.testing.assert_allclose(x,[.31,.69,.3])
    np.testing.assert_allclose(v,[-1.,1.,3.])

def test_ballistic_energy_and_dissipation():
    elastic=m.bounce_run(1)
    damped=m.bounce_run(.7)
    np.testing.assert_array_equal(elastic['positions'][0],damped['positions'][0])
    np.testing.assert_allclose(elastic['energy'],elastic['energy'][0],rtol=0,atol=1e-11)
    assert np.all(np.diff(damped['energy'])<=1e-11)
    assert damped['measure'][-1] < .01
    assert ((damped['positions']>=-1e-12)&(damped['positions']<=1+1e-12)).all()
    no_gravity=m.bounce_run(.7,gravity=0)
    np.testing.assert_allclose(no_gravity['positions'][:,:,1],np.broadcast_to(no_gravity['positions'][0,:,1],no_gravity['positions'][:,:,1].shape))

def test_exact_first_impact():
    # Drop from y=.5 with g=1 reaches the floor at t=1.
    y,v=m.vertical_step(.5,0,1.1,1,.7)
    np.testing.assert_allclose([y,v],[.7*.1-.5*.1**2,.7-.1],atol=1e-12)

def student_scope():
    n=nbformat.read(R/'notebooks/12_build_simulation.ipynb',as_version=4)
    scope={'np':np}
    for c in n.cells:
        if c.cell_type=='code' and c.source.startswith(('def move(', 'def wall(', 'def my_simulation(', 'def check_student_code(')):
            exec(c.source,scope)
    return scope,n

def test_incomplete_student_code_cannot_pass():
    scope,_=student_scope()
    assert scope['student_ready'] is False
    assert scope['my_simulation'](.2,.3,.1,.2,.02,5) is None

def test_student_checks_accept_reference_and_reject_wrong_motion():
    scope,n=student_scope()
    exec((R/'mentor/coding_reference.py').read_text(),scope)
    assert scope['check_student_code']()
    scope['move']=lambda position,velocity,dt:position-velocity*dt
    assert not scope['check_student_code']()

def test_primary_notebooks_embed_engine_and_no_hidden_solution():
    engine=(R/'simulation/teaching_particles.py').read_text().strip()
    for name in ['10_home_explore','11_home_compare','12_build_simulation','student_workbook_he']:
        n=nbformat.read(R/f'notebooks/{name}.ipynb',as_version=4)
        assert sum(c.cell_type=='code' and c.source==engine for c in n.cells)==1
        assert not any('coding_reference' in c.source for c in n.cells)
        nbformat.validate(n)
