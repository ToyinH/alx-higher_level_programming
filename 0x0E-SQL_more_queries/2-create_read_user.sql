-- Create or modify database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create or modify user user_0d_2 with the password 'user_0d_2_pwd'
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant SELECT privilege to user_0d_2 on the hbtn_0d_2 database
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
