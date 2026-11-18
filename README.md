# אלפא — מעבדה חישובית לתלמידים

שלושה תרגילים בעברית: פותחים מחיצה בין חלקיקים, משנים חוק קפיצה, וכותבים סימולציה בעזרת פונקציות ולולאה. המסלול מתאים לתלמידים שמכירים משתנים, תנאים ולולאות.

## מתחילים כאן

**[פתיחת המחברת האינטראקטיבית בעברית ב־Colab](https://colab.research.google.com/github/yaminbens/alpha-mentorship/blob/main/notebooks/student_workbook_he.ipynb)**

המחברת כוללת את ההסברים, האנימציות, קטעי הקוד להשלמה, הבדיקות ותאי התיעוד. ב־GitHub רואים תצוגה מקדימה; כדי להריץ ולערוך לחצו על הקישור ושמרו עותק אישי באמצעות **File → Save a copy in Drive**. אין צורך להתקין תוכנה או לטעון קובץ מצב התחלתי.

**[דפי ההוראות בתוך GitHub](site/pages/index.md)** · **[אתר התלמידים](https://yaminbens.github.io/alpha-mentorship/)** · **[שמירה ושיתוף](site/pages/submit.md)**

| שלב | הפעילות | מחברת נפרדת |
|---|---|---|
| [פתיחה](site/pages/task-0.md) | משנים משתנה, מוסיפים שורת קוד ושומרים גרף | [Colab](https://colab.research.google.com/github/yaminbens/alpha-mentorship/blob/main/notebooks/00_getting_started.ipynb) |
| [תרגיל 1 — פתיחת מחיצה](site/pages/task-1.md) | חוקרים ערבוב, משלימים ספירה ומוסיפים גרף | [Colab](https://colab.research.google.com/github/yaminbens/alpha-mentorship/blob/main/notebooks/10_home_explore.ipynb) |
| [תרגיל 2 — חוק הקפיצה](site/pages/task-2.md) | יוצרים קפיצות מתמשכות או דעיכה ומשווים ריצות בלולאה | [Colab](https://colab.research.google.com/github/yaminbens/alpha-mentorship/blob/main/notebooks/11_home_compare.ipynb) |
| [תרגיל 3 — כותבים סימולציה](site/pages/task-3.md) | משלימים תנועה וקירות, בונים לולאת זמן ובודקים את הקוד | [Colab](https://colab.research.google.com/github/yaminbens/alpha-mentorship/blob/main/notebooks/12_build_simulation.ipynb) |

אפשר להשתמש במחברת המרכזית לאורך כל המסלול, או במחברות הנפרדות. את התרגילים המלאים מבצעים בבית בכמה מפגשים; אין צורך להספיק את כולם בשיעור הראשון.

## שמירה וסקירת העבודה

שומרים את העותק האישי ב־Drive, את הקוד והתשובות, ומורידים את קובצי האנימציה, הגרפים, הנתונים ותנאי הריצה. משתפים את המחברת ותיקיית הקבצים עם החשבון שהמנחה מסר ושולחים קישור בערוץ הפרטי שסוכם. אין לפרסם הגשות או פרטים אישיים במאגר הציבורי.

אם Colab אינו מצליח לפתוח את הקישור, השתמשו ב״הורדת המחברת״ בדף התרגיל באתר, פתחו [Colab](https://colab.research.google.com/) ובחרו **File → Upload notebook**. שמרו לאחר מכן עותק ב־Drive.

## למנחה

- [מדריך המסלול החדש והצעות למשוב](mentor/hebrew_coding_track.md)
- [הנחיות בדיקה ופתרון לדוגמה](mentor/coding_reference.py) — חומר ציבורי לעיון לאחר ניסיון עצמאי.
- [תוכנית המפגש הראשון — שעה](meetings/01_introduction/agenda.md)
- [המצגת](https://yaminbens.github.io/alpha-mentorship/presentation/slides.html) ו[הדגמת המנחה](meetings/01_introduction/demonstration.md)
- [מדריך סקירת הגשות](mentor/review_workflow.md) ו[פתרון תקלות](mentor/troubleshooting.md)
- [חומר מדעי להמשך](site/pages/next.md), כולל סימולציה עם כוחות בין חלקיקים. מחברות ההרחבה באנגלית.
- [המסלול הקודם בסימולטור הדפדפן](archive/browser_track/README.md), שנשמר בנפרד.
- [מצב הפרויקט והבדיקות](STATUS.md)

המודלים החדשים נועדו ללימוד כלים: אין בהם כוחות בין חלקיקים. אין לפרש ערבוב כהתכה או חלקיקים ליד הרצפה כמוצק. המצגת והדגמת הדפדפן נשמרו כחומר מבוא למודל מולקולרי אחר.

## פיתוח ופרסום

המאגר עצמאי ואינו תלוי ב־GNN. אין צורך ב־GPU. קוד המנוע נמצא ב־[simulation/teaching_particles.py](simulation/teaching_particles.py) ומוטמע במחברות כדי לאפשר הרצה עצמאית.

```sh
python -m pip install -r requirements.txt
python tools/make_notebooks.py
python tools/build_site.py
python -m pytest tests -q
python tools/check_notebooks.py
python -m http.server 8000 --directory dist
```

הגדרות המאגר והשיתוף נמצאות ב־[site/config.json](site/config.json). דחיפה לענף `main` בונה ומפרסמת את האתר. דפי המקור משתמשים בקישורים אמיתיים בתוך GitHub; הבנייה ממירה אותם לכתובות האתר. ראו [הנחיות עריכה](CONTRIBUTING.md), [רישיון](LICENSE) ו[מקורות חיצוניים](THIRD_PARTY.md).
