1) Finding elements
BY CSS SELECTOR

* find by id
$$("div[id='login-field'])
$$("#login-field")

* by class
$$(".some-class")

* use attributes
$$("div[class='some_div']")

* find among same elements
$$("button[class='primary']:nth-child(1)")
$$("button[class='primary']:nth-of-type(5)")

* chain locators together
$$("button[id='special-button'] > .some-class > div[name='currency-field']")
$$("button[id='special-button']  .some-class  div[name='currency-field']")

BY XPATH
* find by attribute
$x("//div[@id='login-field']")

* find among same elements
$x("button[3]")

* move up the tree
$x("//input[@id='password']/ancestor::div")

* move down the tree
$x("//input[@id='password']/descendant::div")

* chain locators togeter
* look for direct child of the node
$x("//button[@class='primary']/span[2]")
* look for any descendant
$x("//button[@class='primary']//span[2]")

* find by text
$x("//*[contains(text(), 'Admin interface')]")