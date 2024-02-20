# OnlineStatusFaker

Your Slack and Teams online status never changes to red anymore. You stay always logged in and green.

### Requirements

```
pip install pynput
pip install pyautogui
```

### Run

After running the application switch the focus to the slack or team application. After 10 seconds you will see magically the cursor pointer jumping up and down.
By pressing the **ESC** key on your keyboard the application will be closed.

```
$: python main.py
```


### Output 

```
Starting Online-Faker in 10 seconds...
You can quit the application pressing the ESC or CTRL key.
10
9
8
7
6
5
4
3
2
1
Mouse started...
ESC pressed. Quitting the application.
```