Feature: tutorial ของการทํา behave และ selenium

    Scenario: ตรวจสอบว่าหน้าเว็บที่เข้าไปมี title เหมือนที่คาดว่าหรือไม่
        Given ฉันเข้าไปที่หน้าเว็บ form ของ selenium
        Then ฉันจะเห็นว่าในหน้าเว็บมี heading ที่เขียนว่า Web form

    Scenario: สามารถใส่คำลงไปใน text input แล้วกด Submit ได้
        Given ฉันเข้าไปที่หน้าเว็บ form ของ selenium
        Then ฉันใส่คำว่า "CS364" ลงใน text input
        And ฉันกดปุ่มที่เขียนว่า Default checkbox
        And ฉันกดปุ่ม Submit
        Then ฉันควรจะเห็น message ขึ้นว่า "Received!"

