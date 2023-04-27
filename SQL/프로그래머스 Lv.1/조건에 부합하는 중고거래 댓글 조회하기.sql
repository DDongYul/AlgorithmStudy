--USED_GOODS_BOARD와 USED_GOODS_REPLY 테이블에서 2022년 10월에 작성된 게시글 제목,
--게시글 ID, 댓글 ID, 댓글 작성자 ID, 댓글 내용, 댓글 작성일을 조회하는 SQL문을 작성해주세요.
--결과는 댓글 작성일을 기준으로 오름차순 정렬해주시고,
--댓글 작성일이 같다면 게시글 제목을 기준으로 오름차순 정렬해주세요.

SELECT B.TITLE,B.BOARD_ID,R.REPLY_ID,R.WRITER_ID,R.CONTENTS,date_format(r.created_date,'%Y-%m-%d')
FROM USED_GOODS_BOARD B,USED_GOODS_REPLY R
WHERE B.BOARD_ID = R.BOARD_ID AND B.CREATED_DATE like "2022-10-%%"
order by R.CREATED_DATE,B.TITLE