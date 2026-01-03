# 寫SQL時建議的優良習慣
## 可讀性 (Readable SQL 是第一優先)
+ 關鍵字全部大寫
+ 一行一個語意單位
    ```SQL
    SELECT
        id,
        name
    FROM users
    WHERE 
        age > 18
        AND status = 'active';
    ```
    + 一般習慣是先寫「等值條件」，再寫「範圍條件」。
+ 明確使用 table alias
+ 資料正確性：永遠明確 JOIN 條件
+ 小心 NULL