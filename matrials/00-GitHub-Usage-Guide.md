# دليل استخدام GitHub — مستودع NTI_Intenship_ML

> هذا الدليل العملي الخاص بك: من أين تشتغل، وما الأوامر اليومية، وكيف تتجنب الأخطاء التي واجهناها.

## 1. أين تشتغل؟

- الشغل كله داخل: `GITHUB_NTI/NTI` (الفرع `main`)
- الرابط الجديد بعد إعادة التسمية:
  `https://github.com/mohamed-sherif-data/NTI_Intenship_ML`
- الرابط القديم `NTI_GitHub` يحول تلقائيا للجديد، لكن تم تحديث `origin` عندك للجديد.
- ممنوع: إنشاء مجلد `git` جديد في `D:\Desktop\NTI` — هذا كان سبب مشكلة `repo جوه repo`.

## 2. الدورة اليومية (احفظها)

```powershell
cd D:\Desktop\NTI\GITHUB_NTI\NTI
git pull
# ... عدل ملفاتك ...
git status --short
git add .
git commit -m "وصف واضح للتعديل"
git push
```

- `git pull` أولا دائما قبل الشغل.
- `git status --short` قبل كل `commit` لترى ما تغير.
- رسالة الـ `commit` بصيغة الأمر: `Add ...` / `Update ...` / `Fix ...`.

## 3. هيكل المستودع

```
NTI_Intenship_ML/
├── sision.ipynb      # شغلك الأساسي
├── matrials/         # ماتريالز التدريب (17 مجلدا + TimeLine.txt)
├── Excersizes/       # تمارينك (فارغ حاليا)
├── .gitattributes    # إعدادات Git
└── .gitignore        # (يُنصح بإضافته — انظر below)
```

## 4. يُنصح بإضافة .gitignore

```gitignore
.ipynb_checkpoints/
__pycache__/
*.pyc
.venv/
```

## 5. أخطاء تتجنبها (من تجربتك)

| الخطأ | ما حدث | الحل |
|---|---|---|
| `repo جوه repo` | مجلد `.git` خارجي + داخلي، وخطأ `no submodule mapping` | حذفنا `.git` الخارجي — لا تنشئ `git init` في `D:\Desktop\NTI` أبدا |
| تغيير اسم المستودع | الرابط القديم `NTI_GitHub` بقي في `origin` | حدثناه بـ `git remote set-url origin ...NTI_Intenship_ML.git` |
| حذف ملف بالخطأ (`sision.ipynb`) | ظهر `deleted` في `git status` | الاسترجاع: `git restore <file>` قبل الـ `commit` |
| رفع بيئة العمل | مجلد `.venv` كبير جدا | لا تضعه داخل المستودع أبدا |

## 6. أوامر الطوارئ

```powershell
git restore sision.ipynb        # استرجاع ملف محذوف قبل commit
git log --oneline -5            # آخر 5 commits
git remote -v                   # التأكد من الرابط
```

## 7. قاعدة README الجيدة (من سكيل readme-optimization)

- أول سطر يشرح: ما هذا؟ ولماذا؟
- أمر تشغيل واحد ينسخ ويعمل خلال دقيقة.
- حالة صادقة: `Learning / Experimental` — لا تكتب `production-ready`.
- لا بادجات كثيرة بلا معنى.
- المصدر: `README` صفحة هبوط + توجيه، وليس توثيقا كاملا.
