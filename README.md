# SeleniumTestting
Created 3 files, for everyone who should create a test in selenium.
I added a driver folder. where the correct driver is for version '101.0.4951'. Please install the correct driver if u have anything different.
Too lazy to install? Add this to ur code as the driver instead of the driver from the driver file.
```python
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
```
Goodluck have fun :)