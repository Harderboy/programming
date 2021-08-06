SELECT CONCAT(
   "*6\r\n",
   '$',LENGTH(redis_cmd),'\r\n',redis_cmd,'\r\n',
   '$',LENGTH(redis_key),'\r\n',redis_key,'\r\n',
   '$',LENGTH(hkey1),'\r\n',hkey1,'\r\n','$',LENGTH(hval1),'\r\n',hval1,'\r\n',
   '$',LENGTH(hkey2),'\r\n',hkey2,'\r\n','$',LENGTH(hval2),'\r\n',hval2,'\r' # 最后一行没有 \n
)FROM(
   SELECT 'HMSET' AS redis_cmd,
   concat_ws(':','code', id) AS redis_key,
   'id' AS hkey1, id AS hval1,
   'coupon_code' AS hkey2, coupon_code AS hval2
   from code
)AS t