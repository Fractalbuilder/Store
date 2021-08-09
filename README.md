# Why This Is Not Project 2

Please pay special attention to the “Complexity” section in which I consider are the main reason to accept this project.

## Features not present in project 2
* Product rating: Products have a rating feature which consists of 5 stars.

* Product filter: In each product category the user is provided with a custom set of options to filter the type of product they are searching for.

* Ads: An animated advertisement is visible at the top of the page.

* Corporate identity: The esthetics have been carefully designed to be consistent and applicable to all elements, so that there’s a resemblance between them in the way they look and behave, for example when they are affected by the responsive design.

## Difference in requirements

### Product features
| Project 2 | Project Final |
| ------ | ------ |
| All items have the same set of features | The products belonging to a category have different features respect to products of other categories |

### Product selection
| Project 2 | Project Final |
| ------ | ------ |
| A unique product is selected (bid) and is bought once | More than one item of the same product can be selected, and later this quantity can be modified and finally the purchase is made, afterwards depending on stock the product can be selected and bought all the times the user want  |

### Category 
| Project 2 | Project Final |
| ------ | ------ |
| Every category has its set of articles and these can be searched based on their category | Categories can consist of products or subcategories, and every category provides the path of all its parent categories |

### Responsive design
| Project 2 | Project Final |
| ------ | ------ |
| Responsive design is apply to general areas to keep the page in order | Responsive design is applied even to the smaller elements, so this way individual texts get vertical padding spaces when necessary after line jumps in wrapped divs |

## Complexity
* The product rating feature doesn’t depend only on the current user opinion but on all other users rating the product, so this is not just a matter of adding or deleting a unit from the database.

* The way a product information is managed and gathered from the database depends on the category the product belongs to. The filter options for example of a laptop (Ram, screen size, etc) aren't the same for an HDD, besides in each category the user can freely use one, some or all filters, or don’t use any at all, the way this is dynamically managed without overwhelming the database with the inclusion of every product filter in the sent queries is more complex than just creating static html templates for each possible option. The common information to all kinds of products such as price and stock is stored in the Product model, but product specific information is stored in custom models as LaptopFeatures, for this reason crossed model queries are issued when products are filtered out and this queries must be dynamically created.

* The ad is a SVG element in which its internal objects are animated individually, and it’s adjusted so that it’s compatible with the responsive design model of the page. This is critical because the SVG structure is not compatible by default with changes in the layout such as the produced by the responsive design, aspect ratio and viewport issues will arise if not properly setup.

* The nature of the multiselection process in which multiple items of the same products can be selected at the time with multiple different products and buy them all at once, make the acquisition of elements much more complex in the final project than in project 2.

* Each category must dynamically work out what type of subcategories it stores, sometimes both a category with subcategories and a category with products, for example the category “Computers and Accessories” stores the Computers category (Linking to a page with more subcategories), and the “Data Storage” category (Linking to a page with products), in this case the “Computers and Accessories” must apply the proper links to each of its subcategories. 

* The project 2 consisted of 5 models and 8 templates, this final project is made up with 12 models and 18 templates.

# Motivation

This is a store web application which supports different tools and approaches to execute the same actions (In different contexts), for example if a user wants to modify the quantity of a product, they can modify this value from the product page or from the bills page, so that it’s comfortable for them to apply changes without needing to traverse all along the app to do it; this is the case for example with the categories path, or the products themself. At the moment the user is assumed to have enough credit for any purchase, so when the pay action is executed the bill is automatically generated. The payment is a feature that will be included in future versions of the app. The project integrates different technologies making use of the Python API, promises, responsive design, MD files visualization, pagination, local and on cloud sources (Some parts of the same page take sources from the localhost, cloud and the database).

When I created this project I had in mind to work on something really useful, something I really will use in the future. By now I will include it as part of my portfolio to show potential customers my skills, and build it up to the point that the project is commercially viable. I have a specific interest in commercial projects because this is something on growing demand in the current days, and where I live this is possibly what I will turn out doing for a living.


# The project

If not explicitly stated users who are not logged in can’t see the pages. This webapp fulfils the next requirements:

* __New products page:__ All available products are shown starting with the newest ones. This section includes pagination so that only 6 products are present at the time, and all items are design responsive. Users who are not logged in can see this page.

* __Image alternative:__ This is an image to be displayed when no image is provided for a product or if a problem arises fetching the image from an external server.

* __Ad:__ This is a SVG image which belongs to the layout. The ad is continuously animated and has a responsive design.

* __Categories page:__ All the paths to the current category must be visible all the time, so that the user can visit at will any category the path is made up. In the categories tree there're leaf categories, these are the ones which lead to products instead of intermediate categories, so clicking on a leaf category must take the user to a page where all products included in the category are presented. Users who are not logged in can see all pages included in this point.

* __Category page:__ All the paths to the current category must be visible all the time, so that the user can visit at will any category the path is made up. Custom filters are provided based on the category, and in the case of options with min and max values these must be checked to assure min isn’t bigger than max. The user can freely use any combination of the given filter options. This section includes pagination so that only 6 products are present at the time, and all items are design responsive. Users who are not logged in can see all pages included in this point.

* __Product page:__ This page includes information about the product such as name, pic, short description, price, and items in stock. The product’s full description must be read from MD files in a local location, so that these can be easily edited by the employees in charge without the need to access the application, and they can create an attractive design with the rich features of the MD format. In this section all items are design responsive. Users who are not logged in can see this page.

    - Add tab. If the product is in stock a button lets the user add a single item to the cart, after an item is added options to modify the quantity of items and delete them are provided. If the quantity is set as 0 this is equivalent to press the “remove from cart” button. If the quantity is set to a value greater then the items in stock, the quantity is set as the number of items in stock.

    - Comment tab. The user can add a comment and visualize previous comments.

   - Rating. The user can rate their satisfaction with the product voting in a 5 star rating feature. Only the users who have bought the product can rate the product and afterwards this rating can be changed anytime. If an anonymous user attempts to vote a message must show up indicating that only logged in users can vote. The rating is an average of all user votes. When a vote is successful a message must show up as a confirmation. When hovering over the rating feature the pointed stars must be highlighted, to provide the user with a graphical reference of their selection.
 
* __Bills page:__ This page includes the cart section and bills section. In this section all items are design responsive.

    - Cart section. This section is presented only if there’s any product added to the cart. Each cart detail (A field with the information of a single product) includes the product name, quantity, unit price, total price, and has options to modify the quantity of the item and delete it. If the quantity is set as 0 this is equivalent to press the “remove” button. If the quantity is set to a value greater then the items in stock, the quantity is set as the number of items in stock. At the end the total price of the cart is shown (The sum of prices of all cart details). Clicking the pay button passes the cart information to a bill and deletes the cart in use.

    - Bills section. This section is presented only if there are bills available. This section includes information about the bill such as id, creation date and total price.