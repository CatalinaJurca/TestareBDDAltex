  #Test 6: Intrati pe altex.ro, dati click pe linkul Contact, si verificati faptul ca nu puteti sa dati submit la formular daca nu sunt completate campurile obligatorii (verificati ca ramaneti pe aceeasi pagina)
Feature:Feature will validate the contact module of Altex page
Scenario: Verify the submit contact form without filling the required fields
  Given I am on the Altex homepage
  When I go to the contact form
  And I fill the required fields without one
  Then The page is not changing