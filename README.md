# CheckThisOut330 의 이미지 처리 소프트웨어

[CheckThisOut330](https://github.com/CheckThisOut330/CheckThisOut330) 으로 데이터를 넘겨주는 이미지 처리 소프트웨어<br>
학교 인터넷으로 포트포워딩 하기 번거로워서 웹서버와 이미지 처리 서버를 분리시킨 구조로 포트포워딩이 가능하고 서버 사양이 넉넉하다면 두개의 소프트웨어를 하나로 합쳐도 무방함

### 사용법

1. 필요한 모듈 설치
2. `self.cam_ip` 에 "방 번호": "ip 주소" 형식으로 추가
3. `self.server_link` 에 [CheckThisOut330](https://github.com/CheckThisOut330/CheckThisOut330) 을 실행한 서버 링크를 입력
4. 실행

### 문제
시간상의 문제로 \[카메라 서버 <-> 이미지 처리서버\], \[이미지 처리 서버 <-> 웹 서버\] 의 통신에서 보안 문제를 고려하지 않았으므로 실제 사용해야 할 경우 이에 대해 수정이 필요함
