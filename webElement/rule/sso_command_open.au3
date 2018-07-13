#include <WinAPIFiles.au3>

;从cmd命令行传参 $CmdLine[1] 代表命令行输入的第一个内容
$iconType = $CmdLine[1]
$username = $CmdLine[2]
$pwd = $CmdLine[3]
$cmdList = $CmdLine[4]

;等待窗口被激活
Func wait_windows_active($iconType)
	If $iconType == "putty" Then
		If WinExists("PuTTY Security Alert") Then
			$hWnd = WinGetHandle("PuTTY Security Alert")
			ControlClick($hWnd, "", "Button1")
		EndIf
		$hWnd = WinWait("[CLASS:PuTTY]", "", 10)
	ElseIf $iconType == "secureCRT" Then
		$hWnd = WinWait("[CLASS:VanDyke Software - SecureCRT]", "", 10)
	EndIf

	;$hWnd = WinWait($iconType, "", 10)
	;$hWnd = WinWait("[CLASS:" & $iconType & "]", "", 10)

	WinActivate($hWnd)
EndFunc


;输入账号
Func enter_username($username)
	Sleep(2000)
	Send($username)
	Sleep(1000)
	Send("{ENTER}")
	Sleep(1000)

EndFunc

;输入密码
Func enter_pwd($pwd)
	Sleep(2000)
	Send($pwd)
	Sleep(3000)
	Send("{ENTER}")
	Sleep(3000)
EndFunc

Func writeTmpTxt($cmdList)
	$tmpPath = "D:\testIsomp\webElement\sso\sso1.txt"
	Local $hFileOpen = FileOpen($tmpPath, $FO_APPEND)
	If $hFileOpen <> -1 Then
		FileWriteLine($hFileOpen, $cmdList)
	EndIf
	FileClose($hFileOpen)
EndFunc

;执行输入的命令
Func excute_cmd($cmdList)
	$recmdList = StringSplit($cmdList,",", $STR_NOCOUNT  )
	Sleep(5000)
	For $cmdStr in $recmdList
		;writeTmpTxt($cmdStr)
		Sleep(2000)
		Send($cmdStr)
		Sleep(2000)
		Send("{ENTER}")
		Sleep(2000)
	Next
EndFunc

;关闭窗口
Func close_windows($iconType)
	If $iconType == "putty" Then
		$hWndType = WinWait("[CLASS:PuTTY]", "", 10)
	ElseIf $iconType == "secureCRT" Then
		$hWndType = WinWait("[CLASS:VanDyke Software - SecureCRT]", "", 10)
	EndIf

	Sleep(1000)
	WinKill($hWndType)
	If WinExists("SecureCRT") Then
		$hWnd = WinGetHandle("SecureCRT")
		ControlClick($hWnd, "", "Button1")
	EndIf
	;WinClose($hWndType)
	Sleep(500)
EndFunc

;执行操作
Func cmd_enter($iconType,$username,$pwd,$cmdList)

	wait_windows_active($iconType)

	If $username <> "no" Then
		enter_username($username)
	EndIf
	If $pwd <> "no" Then
		enter_pwd($pwd)
	EndIf
	excute_cmd($cmdList)
	;close_windows($iconType)
EndFunc


cmd_enter($iconType,$username,$pwd,$cmdList)
;writeTmpTxt($username)
;writeTmpTxt($pwd)
;writeTmpTxt($cmdList)

;Local $cmdList[] = ["ls -l","ifconfig","exit"]
;excute_cmd($cmdList)