import requests
import json

# MIDAS Gen API 서버 설정
Gen_API_URL = "http://127.0.0.1:10024"

# 문서 열기
def open_document(filepath):
    """MIDAS Gen에서 문서를 엽니다."""
    payload = {"Argument": filepath}
    response = requests.post(f"{Gen_API_URL}/doc/open", json=payload)
    print("문서 열기:", response.text)

# 분석 실행
def run_analysis():
    """열린 문서에 대해 분석을 실행합니다."""
    response = requests.post(f"{Gen_API_URL}/doc/anal", json={})
    print("분석 실행:", response.text)

# 결과 내보내기
def export_results(filepath):
    """분석 결과를 지정된 경로로 내보냅니다."""
    payload = {"Argument": filepath}
    response = requests.post(f"{Gen_API_URL}/doc/export", json=payload)
    print("결과 내보내기:", response.text)

# 예제 실행
if __name__ == "__main__":
    document_path = "C:\\path\\to\\your\\file.mgb"  # MIDAS Gen 문서 경로
    result_path = "C:\\path\\to\\export\\result.json"  # 결과를 내보낼 경로

    open_document(document_path)
    run_analysis()
    export_results(result_path)
