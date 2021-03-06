‫باب یک تلویزیون جدید خریده‌است که n شبکه دارد. اسم هر شبکه یک رشته از حروف انگلیسی کوچک است.

‫کنترل تلویزیون باب یک کلید دارد که شبکه‌ی کنونی را به شبکه‌ی دیگری تغییر می‌دهد (شبکه‌ها به ترتیب از *۱* تا n شماره گذاری شده‌اند). اگر تلویزیون در شبکه‌ی i ام باشد با فشردن کلید آن دو حالت زیر می‌تواند اتفاق بیفتد:

- ‫اگر  i  کمتر از  n  باشد به شبکه‌ی  i+1  تغییر پیدا می‌کند.
- ‫اگر  i  برابر  n  باشد به شبکه‌ی 1 تغییر پیدا می‌کند.

‫اگر تلویزیون در ابتدا xامین شبکه را نشان‌دهد، نام شبکه‌ای که پس از آن که *باب* کلید کنترل تلویزیون را k بار بفشارد تلویزیون نمایش می‌دهد، چه خواهد‌بود؟

# ورودی

‫ابتدا n داده می‌شود که برابر تعداد شبکه‌های تلویزیون است. سپس x داده می‌شود که شماره‌ی شبکه‌ی اوّلیه‌ی تلویزیون است. سپس k که تعداد دفعاتی است که *باب* کلید کنترل تلویزیون را می‌فشارد.

‫سپس n رشته که در i-امین خط بعد نام شبکه‌ی i-ام داده‌ می‌شود. طول نام هر شبکه حداکثر 100 است و نام هیچ دو شبکه‌ای یکسان نیست.

1 ≤ n, k ≤ 100

1 ≤ x ≤n

# خروجی

‫در تنها خط خروجی نام شبکه‌ای که تلویزیون پس از k بار فشردن کلید تلویزیون، نمایش خواهد داد را چاپ کنید.

# مثال

## ورودی نمونه

```
5 2 5
bob
carl
kevin
phil
tim
```

## خروجی نمونه

```
carl
```

‫شبکه ها این گونه تغییر می‌کنند:  

```
 carl > kevin > phil > tim > bob > carl
```