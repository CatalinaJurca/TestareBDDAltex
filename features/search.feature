
Feature: Validate product search results
  # Test 1: cautati un produs la alegere si verificati ca s-au returnat cel putin 10 rezultate

Scenario:Search for a product and check the return of at least 10 results
  Given I am on the Altex homepage
  When I type "frigider" in the search input box and press enter
  Then I get the number of results

  #Test 2: faceti filtrare dupa pret si verificati faptul ca toate produsele returnate au pretul in intervalul de filtrare

Scenario: Filter search by price and check the products prices are the selected range of prices
  Given I am on the Altex homepage
  When I type "frigider" in the search input box and press enter
  And I check the price box between "2000-3000"
  Then The filtering by price is done correctly

  #Test 3: Cautati un produs care nu exista si verifica faptul ca mesajul returnat este: "NE PARE RĂU, NU EXISTĂ PRODUSE ÎN ACEASTĂ CATEGORIE."

Scenario: Search for unexisting product and validate the return message
  Given I am on the Altex homepage
  When I type "cheile genelor" in the search input box and press enter
  Then I get the message "Ne pare rau, cautarea ta "cheile genelor" nu a avut niciun rezultat."

  #Test 4: Cautati un produs, sortati lista de rezultate in ordine crescatoare dupa pret si verificati faptul ca produsele au fost intr-adevar sortate

Scenario: Search and sort by price in ascending order
  Given I am on the Altex homepage
  When I type "laptop" in the search input box and press enter
  And I sort by "Price" ascending
  Then The sorting is done correctly


  #Test 5: Cautati un produs, sortati lista de rezultate in ordine descrescatoare dupa pret si verificati faptul ca produsele au fost intr-adevar sortate

Scenario: Search and sort by price in descending order
  Given I am on the Altex homepage
  When I type "laptop" in the search input box and press enter
  And I sort by "Price" descending
  Then The sorting is done correctly

