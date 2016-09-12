### Name:
    Kiran reddy

### Ip Address
    159.203.187.231

### Phpmyadmin Link
    http://159.203.187.231/phpmyadmin

## Table Create statements

#### gift_options.sql

...sql
CREATE TABLE IF NOT EXISTS gift_options (
allowGiftWrap boolean NOT NULL,
allowGiftMessage boolean NOT NULL,
allowGiftReceipt boolean NOT NULL
 primary key(allowGiftReceipt)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
