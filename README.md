SELECT
c.id AS customer_id,
c.username AS customer_name,
SUM(f.qty * rci.item_cost) AS points_redeemed,
GROUP_CONCAT(CONCAT(rci.item_name, ' (', f.qty, ')') SEPARATOR ', ') AS fulfilled_items
FROM
customers c
JOIN fulfillment f ON c.id = f.customer_id
JOIN rewards_catalog_items rci ON f.reward_catalog_item_id = rci.id
GROUP BY
c.id, c.username;
