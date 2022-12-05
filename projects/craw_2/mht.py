import os, sys
from win32com.client.gencache import EnsureDispatch as Dispatch

URL = r"https://www.ruanyifeng.com/blog/2019/08/weekly-issue-70.html"
FILEPATH = r"test.mht"

message = Dispatch("CDO.Message")
message.CreateMHTMLBody(URL)
stream = Dispatch(message.GetStream())
stream.SaveToFile(FILEPATH, 2)
stream.Close()
