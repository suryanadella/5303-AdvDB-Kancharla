### Name:
    Kiran reddy

### Ip Address
    159.203.187.231

### Phpmyadmin Link
    http://159.203.187.231/phpmyadmin

## Table Create statements

#### gift_options.sql

```sql
CREATE TABLE IF NOT EXISTS gift_options(
	itemId INT( 10 ) NOT NULL ,
	allowGiftWrap BOOLEAN NOT NULL ,
	allowGiftMessage BOOLEAN NOT NULL ,
	allowGiftReceipt BOOLEAN NOT NULL ,
	PRIMARY KEY ( itemId ) ,
	FOREIGN KEY ( itemId ) REFERENCES products( itemId )
) ENGINE = INNODB DEFAULT CHARSET = latin1;
```

#### image_entities.sql

```sql
CREATE TABLE IF NOT EXISTS image_entities (
	itemId INT( 10 ) NOT NULL ,
        thumbnailImage varchar(149) NOT NULL,
        mediumImage varchar(149) NOT NULL,
        largeImage varchar(149) NOT NULL,
        entityType varchar(9) NOT NULL,
    	PRIMARY KEY ( itemId ) ,
	FOREIGN KEY ( itemId ) REFERENCES products( itemId )
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
```

#### market_place_price.sql

```sql
CREATE TABLE IF NOT EXISTS market_place_price(
	itemId INT( 10 ) NOT NULL ,
	price DOUBLE NOT NULL ,
	sellerInfo VARCHAR( 50 ) NOT NULL ,
	standardShipRate DOUBLE NOT NULL ,
	twoThreeDayShippingRate DOUBLE NOT NULL ,
	availableOnline BOOLEAN NOT NULL ,
	clearance BOOLEAN NOT NULL ,
	offerType VARCHAR( 20 ) NOT NULL ,
	PRIMARY KEY ( itemId ) ,
	FOREIGN KEY ( itemId ) REFERENCES products( itemId )
) ENGINE = INNODB DEFAULT CHARSET = latin1;
```	


#### products.sql

```sql

CREATE TABLE IF NOT EXISTS products (
	itemId int(10) NOT NULL,
	parentItemId int(10) NOT NULL,
	name varchar(250) NOT NULL,
	salePrice float(6,2) NOT NULL,
	upc bigint(12) NOT NULL,
	categoryPath varchar(123) NOT NULL,
	shortDescription text(1200) NOT NULL,
	longDescription text(6000) NOT NULL,
	brandName varchar(36) NOT NULL,
	thumbnailImage varchar(149) NOT NULL,
	mediumImage varchar(149) NOT NULL,
	largeImage varchar(149) NOT NULL,
	productTrackingUrl varchar(450) NOT NULL,
	modelNumber varchar(60) NOT NULL,
	productUrl varchar(350) NOT NULL,
	categoryNode varchar(25) NOT NULL,
	stock varchar(13) NOT NULL,
	addToCartUrl varchar(240) NOT NULL,
	affiliateAddToCartUrl varchar(300) NOT NULL,
	offerType varchar(20) NOT NULL,
	msrp double NOT NULL,
	standardShipRate double NOT NULL,
	color varchar(12) NOT NULL,
	customerRating varchar(6) NOT NULL,
	numRevieus int(6) NOT NULL,
	customerRatingImage varchar(50) NOT NULL,
	maxItemsInOrder int(6) NOT NULL,
	size varchar(50) NOT NULL,
	sellerInfo varchar(50) NOT NULL,
	age varchar(16) NOT NULL,
	gender varchar(6) NOT NULL,
	isbn bigint(16) NOT NULL,
	preOrderShipsOn varchar(20) NOT NULL,
	primary key(itemId,parentItemId)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
```
