from ctypes import windll

# DLL 경로 지정
dll_path = r"c:\users\hyagnlee0508\appdata\local\programs\python\python37-32\lib\site-packages\bangtal.dll"

try:
    windll.LoadLibrary(dll_path)
    print("DLL 파일 로드 성공!")
except Exception as e:
    print(f"DLL 로드 실패: {e}")

    # 난 요즘 노트북으로 계속 작업하는데\n빛이 너무 강해서 그런가 눈이 너무 아파서\n소파에서 가끔씩 쉬면서 해\n