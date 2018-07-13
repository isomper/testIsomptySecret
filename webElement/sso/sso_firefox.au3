
;火狐sso弹出框
$title ="启动应用程序"
$hWnd = WinWait($title, "", 10)
WinActivate($hWnd)
If Not WinActivate("$title","") Then  WinActivate("$title","")
#cs
For $i=1 To 4
	Send("{TAB}")
	Sleep(500)
Next
#ce
Sleep(1000)
Send("{ENTER}")