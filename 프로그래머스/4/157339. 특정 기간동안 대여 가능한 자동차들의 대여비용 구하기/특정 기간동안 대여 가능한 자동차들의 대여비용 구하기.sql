SELECT A.CAR_ID, A.CAR_TYPE, 
ROUND((A.DAILY_FEE*(1-C.DISCOUNT_RATE / 100)*30),0) AS FEE
FROM CAR_RENTAL_COMPANY_CAR AS A
LEFT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS B
ON A.CAR_ID = B.CAR_ID AND START_DATE<='2022-11-30' AND END_DATE>='2022-11-01'

INNER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS C
ON A.CAR_TYPE = C.CAR_TYPE AND C.DURATION_TYPE = '30일 이상'

WHERE 500000<=(A.DAILY_FEE*(1-C.DISCOUNT_RATE / 100)*30) AND 
(A.DAILY_FEE*(1-C.DISCOUNT_RATE / 100)*30) <2000000 AND
A.CAR_TYPE IN ('세단', 'SUV') AND B.HISTORY_ID IS NULL
ORDER BY FEE DESC, A.CAR_TYPE, A.CAR_ID DESC