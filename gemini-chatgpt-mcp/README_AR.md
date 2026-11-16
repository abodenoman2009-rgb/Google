# خادم Gemini MCP لربط Google AI Studio مع ChatGPT

هذا مشروع خادم MCP وسيط: يستقبل طلبات ChatGPT عبر MCP ثم يرسلها إلى Gemini باستخدام مفتاح Google AI Studio.

## الأدوات المتاحة داخل ChatGPT
- `ask_gemini(prompt, model)` لإرسال سؤال إلى Gemini واستلام الإجابة.
- `list_gemini_models()` لعرض نماذج مقترحة.

## 1) إنشاء مفتاح Gemini
1. افتح https://aistudio.google.com/app/apikey
2. أنشئ API key.
3. احتفظ بالمفتاح سرياً. لا تضعه داخل الكود أو GitHub ولا ترسله في المحادثة.

## 2) النشر على Railway
1. أنشئ مستودع GitHub جديداً وارفع جميع ملفات هذا المجلد.
2. في Railway اختر New Project ثم Deploy from GitHub Repo.
3. افتح Variables وأضف:
   - `GEMINI_API_KEY` = مفتاح Gemini الذي أنشأته.
4. انتظر اكتمال النشر، ثم افتح Settings/Networking وأنشئ نطاقاً عاماً (Generate Domain).
5. عنوان MCP المتوقع هو:
   `https://YOUR-RAILWAY-DOMAIN/mcp`

## 3) ربطه بـ ChatGPT
1. افتح إعدادات ChatGPT ثم Apps/Connectors (قد يختلف الاسم حسب إصدار الحساب).
2. اختر إضافة تطبيق/موصل مخصص يدعم MCP عبر الإنترنت.
3. أدخل عنوان الخادم:
   `https://YOUR-RAILWAY-DOMAIN/mcp`
4. أكمل خطوات التفويض/الاتصال التي يعرضها ChatGPT.

## ملاحظات مهمة
- هذا المشروع يستخدم Streamable HTTP MCP.
- الخادم لا يطلب من المستخدم مفتاح Gemini داخل المحادثة؛ المفتاح يبقى في متغيرات Railway.
- لا تشارك رابط الخادم إذا لم تضف مصادقة مناسبة. هذا الإصدار الأولي لا يطبق OAuth أو مفتاح دخول خاصاً بعميل MCP؛ استخدمه للاختبار فقط، وأضف طبقة مصادقة قبل الاستخدام العام.
- `healthcheckPath` في إعداد Railway يمكن تغييره إلى `/` أو تعطيله إذا كانت المنصة لا تقبل مسار فحص غير MCP.
- قد تتطلب إتاحة إضافة موصل MCP مخصص في ChatGPT خطة أو إعدادات مساحة عمل تدعم ذلك.
