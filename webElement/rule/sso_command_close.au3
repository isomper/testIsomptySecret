#include <WinAPIFiles.au3>

;从cmd命令行传参 $CmdLine[1] 代表命令行输入的第一个内容
$iconType = $CmdLine[1]
;$username = $CmdLine[2]
;$pwd = $CmdLine[3]
;$cmdList = $CmdLine[4]

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
	WinClose($hWndType)
	Sleep(500)
EndFunc

;执行操作
Func cmd_enter($iconType)
	close_windows($iconType)
EndFunc


cmd_enter($iconType)
;writeTmpTxt($username)
;writeTmpTxt($pwd)
;writeTmpTxt($cmdList)

;Local $cmdList[] = ["ls -l","ifconfig","exit"]
;excute_cmd($cmdList)