#project meno
iframe01의 내용이 iframe02로 가기
<iframe src="iframe01.html" id="popupid01" name="iframe01" width="300" height="400"></iframe>
<iframe src="" id="popupid02" name="iframe02" width="300" height="200"></iframe>
<a href="" onclick="popupid01.iframe01.location.href='iframe01.html';" target="iframe02">팝업창 열기4(iframe01->iframe02)</a>
