from ctypes import windll

# DLL 경로 지정
dll_path = r"c:\users\hyagnlee0508\appdata\local\programs\python\python37-32\lib\site-packages\bangtal.dll"

try:
    windll.LoadLibrary(dll_path)
    print("DLL 파일 로드 성공!")
except Exception as e:
    print(f"DLL 로드 실패: {e}")