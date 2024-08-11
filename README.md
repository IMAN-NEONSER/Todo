# برنامه ToDo

این یک برنامه ساده ToDo است که با استفاده از Django 5.1 و Django REST Framework 3.15 ساخته شده است. این برنامه به کاربران اجازه می‌دهد تا وظایفی را ایجاد کنند و پس از انجام آن‌ها، آن‌ها را از لیست حذف کنند.

## ویژگی‌ها

- **ایجاد وظیفه**: افزودن وظایف جدید به لیست کارها.
- **علامت‌گذاری به عنوان انجام‌شده**: حذف وظایف از لیست با علامت‌گذاری آن‌ها به عنوان انجام‌شده.

## نصب و راه‌اندازی

1. مخزن را کلون کنید:

    ```bash
    git clone https://github.com/yourusername/todo.git
    cd todo
    ```

2. یک محیط مجازی ایجاد کنید:

    ```bash
    python -m venv venv
    source venv/bin/activate  # در ویندوز از `venv\Scripts\activate` استفاده کنید
    ```

3. بسته‌های مورد نیاز را نصب کنید:

    ```bash
    pip install -r requirements.txt
    ```

4. مایگریشن‌ها را اعمال کنید:

    ```bash
    python manage.py migrate
    ```

5. سرور توسعه را اجرا کنید:

    ```bash
    python manage.py runserver
    ```

## نقاط پایانی API

- **GET /tasks/**: دریافت لیستی از تمام وظایف.
- **POST /tasks/**: ایجاد یک وظیفه جدید.
- **DELETE /tasks/{id}/**: حذف یک وظیفه با استفاده از ID آن.

## نحوه استفاده

1. سرور را اجرا کنید:

    ```bash
    python manage.py runserver
    ```

2. مرورگر خود یا Postman را باز کنید و به آدرس `http://127.0.0.1:8000/` بروید تا با API تعامل کنید.

3. برای ایجاد یک وظیفه جدید، یک درخواست POST به `/tasks/` با جزئیات وظیفه در بدنه درخواست ارسال کنید.

4. برای علامت‌گذاری یک وظیفه به عنوان انجام‌شده، یک درخواست DELETE به `/tasks/{id}/` ارسال کنید.

## وابستگی‌ها

- Python 3.x
- Django 5.1
- Django REST Framework 3.15

## مجوز

این پروژه تحت مجوز MIT است. برای جزئیات بیشتر به فایل [LICENSE](LICENSE) مراجعه کنید.

## تماس

اگر سؤالی دارید یا پیشنهادی دارید، می‌توانید با من از طریق ایمیل [your-email@example.com](mailto:your-email@example.com) در تماس باشید.
