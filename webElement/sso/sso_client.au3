
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
		WinActivate($hWnd)
	ElseIf $iconType == "secureCRT" Then
		$hWnd = WinWait("[CLASS:VanDyke Software - SecureCRT]", "", 10)
		WinActivate($hWnd)
		If WinExists("New Host Key") Then
			$hWnd = WinGetHandle("New Host Key")
			Sleep(1000)
			ControlClick($hWnd, "", "Button1")
		EndIf

	ElseIf $iconType == "mstsc" or $iconType == "oracle10g" or $iconType == "B/S" or $iconType == "mysql" Then
		Sleep(6000)
		$hWnd = WinWait("远程桌面连接", "", 10)
		WinActivate($hWnd)
		Sleep(3000)
		ControlClick($hWnd, "", "Button5")
		If WinExists("远程桌面连接") Then
			Sleep(3000)
			ControlClick($hWnd, "", "Button11")
			If WinExists("远程桌面连接") Then
				Sleep(3000)
				ControlClick($hWnd, "", "Button2")
			EndIf
		EndIf
	ElseIf $iconType == "sftp" Then
		$hWnd = WinWait("[CLASS:SunAwtFrame]", "", 10)
		WinActivate($hWnd)
	EndIf
	;WinActivate($hWnd)

	;$hWnd = WinWait($iconType, "", 10)
	;$hWnd = WinWait("[CLASS:" & $iconType & "]", "", 10)
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
	Send($pwd)
	Sleep(1000)
	Send("{ENTER}")
	Sleep(1000)
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
	Sleep(3000)
	For $cmdStr in $recmdList
		;writeTmpTxt($cmdStr)
		Send($cmdStr)
		Sleep(1000)
		Send("{ENTER}")
		Sleep(1000)
	Next
EndFunc

;关闭窗口
Func close_windows($iconType)
	If $iconType == "putty" Then
		$hWndType = WinWait("[CLASS:PuTTY]", "", 10)
	ElseIf $iconType == "secureCRT" Then
		$hWndType = WinWait("[CLASS:VanDyke Software - SecureCRT]", "", 10)
	ElseIf $iconType == "mstsc"  Then
		$hWndType = WinWait("[CLASS:TscShellContainerClass]", "", 10)
	ElseIf $iconType == "oracle10g" or $iconType == "B/S" or $iconType == "mysql" Then
		$hWndType = WinWait("[CLASS:TscShellContainerClass]", "", 10)
		Sleep(20000)
	ElseIf $iconType == "sftp" Then
		$hWndType = WinWait("[CLASS:SunAwtFrame]", "", 10)
	EndIf

	Sleep(2000)
	WinKill($hWndType)
	If WinExists("SecureCRT") Then
		$hWnd = WinGetHandle("SecureCRT")
		ControlClick($hWnd, "", "Button1")
	EndIf
	If WinExists("远程桌面连接") Then
		$hWnd = WinGetHandle("远程桌面连接")
		ControlClick($hWnd,"","Button1")
	EndIf
	If WinExists("提示") Then
		$hWnd = WinGetHandle("提示")
		Sleep(1000)
		Send("{ENTER}")
		;ControlClick($hWnd,"","Button1")
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
	Sleep(1000)
	If $cmdList <> "no" Then
		excute_cmd($cmdList)
	EndIf
	close_windows($iconType)
EndFunc


cmd_enter($iconType,$username,$pwd,$cmdList)
;writeTmpTxt($username)
;writeTmpTxt($pwd)
;writeTmpTxt($cmdList)

;Local $cmdList[] = ["ls -l","ifconfig","exit"]
;excute_cmd($cmdList)