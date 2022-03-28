# Milestone Project Four - Testing

The live site can be viewed here - [The On Call Musician](https://on-call-musician.herokuapp.com/).

[Back to README file.](README.md)

![Site Mockup](/media/site-mockup.png)

## Testing
All my code has been put through the following:

* W3C HTML validation.
* W3C CSS validation.
* JSHint JavaScript validation.
* PEP8 online check.

## Functionality
### Manual Testing
These are the steps I went through testing my website and it's functionality.

**Navigation:**
1.	Checked the navigation bar remains at the top of the page at all times and is never hidden by any other content.
2.	Clicked The On Call Musician logo at varying points to make sure it’s a link back to the home page.
3.  Checked that the three icons linking to the profile page, music library and cart appear at the center of the navigation bar.
    * Checked that they perform as expected for:
        * Unregistered users.
        * Registered users.
        * Admin.
    * Checked that all the hover classes work.
    * Checked that if there are any items in the shopping cart then the price will show on the cart icon.
4.	I’ve clicked on all the links to ensure they do what they're supposed to do.
    * Home takes me to the relevant page. 
    * Tested that the hover classes all work.
5.	Checked that at widths below 992px the navigation bar adapts to something more suited to smaller screen sizes. 
    * Seen that all links are now displayed via a dropdown (hamburger) menu only.
        * Toggled the menu icon button on and off to check it displays and hides the menu accordingly.
        * Clicked all links to test they work as before and as expected.

**Home:**
1.	Checked that the background image isn't pixelated, is positioned well and loads as intended.
2.	Checked the text overlay box appears and that the relevant text and button is visible within it.
    * Tested the call-to-action button and it sends us to the Service page as desired.
    * Checked the hover class on the button works.
    * Checked that at widths below 992px, everything still appears as it should.
3.	Checked that all services are displaying properly.
    * All services are shown as individual cards and are suitably displayed dependant of the breakpoint.

**Services:**
1.	Checked that all services load as expected.
2. Checked that the cards are displayed as intended at varying breakpoints:
    * In three columns on larger screens
    * In two columns on screen widths of 768px
    * In one column on screen widths below 768px.
**Individual product card test (test also conducted on other sections)**
Check that every card contains:
* A product image that adjusts dependant to screen width.
    * Checked that this image also links to the service details page.
    * Shows the service name.
    * Shows the service description.
    * Shows the service price.
    * When admin is logged in, the edit and delete links are shown.
    
**Service detail page:**
1. Checked that the correct service has been loaded.
2. Checked that all relevant information has been loaded and is displayed as expected.
3. Check the card according to the **individual service card test** shown in the products test above as the results and functions are similar.
    * Checked that the service description is displayed as well as all the other information specified in the test.
4. Checked that on screen widths of below 768px the layout adapts and the service's information is now being displayed underneath the products image.
5. Seen that the edit and delete links are displayed for admin users.
    * The Keep Shopping button appears for all users underneath the products card and this takes me back to the Services page.
    * Check that the edit and delete buttons appear for admin only.
        * Checked the edit product button opens the edit product form.
        * Checked the delete product button triggers the deletion modal.
    * Checked that all hover classes work.
**Cart:**
1. Checked the page title is correct.
2.	A Continue Shopping button appears at the bottom of the page taking me back to the Services page.
3.	Checked that if the cart is empty a message relaying this appears.
4.	Checked that if items do exist in the cart then each individual item line has its own row with the following details:
    * Image.
    * Service info should always be displayed.
        * Pressed the remove link:
            * Checked that the item is removed from the cart and is no longer displayed. 
            * Seen that the toast message appears confirming the removal.
            * Checked the rest of the cart reacts accordingly.
    * Checked that the subtotal is always displayed.
5.	Tested that each row is responsive to screen width and the most important information is always displayed.
6.	Checked the totals are shown underneath the last row and are done so in a clear and obvious manner.
8.	Pressed the checkout button at the bottom, this takes me to the checkout page.
**Checkout:**
1.	Tested that each page is fully responsive and everything stacks on top of one another at widths below 768px.
2.	Checked that the order summary section is reflective of the cart page that I’ve just been on.
    * Checked that the order summary title has an item count next to it.
    * Checked that each line item is listed and matches that of what was in the cart.
    * Checked that the subtotal and total all match too.
3.	Adjust cart button takes the user back to the cart page if amendments need to be made.
4.	Checked the form to capture the users details, delivery information and payment details is broken into three sections
    * Details
        * Made up of two input fields: *full name and *email. 
        * Checked if the user is unregistered all fields will be blank showing the placeholders only. 
        * Checked if the user is registered and has ordered something previously from the site then these fields could be pre-populated if they have default billing information saved to their profile.
    * Billing
        * Made up of seven input fields: *phone number, address 1 & 2, *town, county, postcode and *country. Fields marked with a * are required in order to submit the form.
        * Checked that only registered users can access the checkout.
    * Payment
        * One field that takes the card number, the MM/YY and CVC number.
        * Checked that this field is required and will always be blank.
5.	Checked the form validates properly by:
    * Attempting to send an empty form.
    * Attempting to send the form whilst leaving any of the * fields empty.
    * Checking that the email field only accepts something with an @ in it.
    * Attempted to send while leaving the payment field empty. This causes a validation error sent from Stripe.
6.	Checked that registered users have a check box to save billing information
    * Toggled the checkbox to test it works.
7.	Checked that two buttons appear at the bottom of the screen along with a confirmation of the total:
    * Checked the hover classes works.
    * Checked the amounts match throughout.
    * Adjust cart button takes the user back to the cart page in case amendments need to be made.
    * Pressing the complete order button starts the checkout / Stripe’s payment process.
8.	Checked the order processing overlay appears to show that something is happening.
9.	On successful completion of the order I’m sent to the order success page where a summary of the order is displayed.
10.	Checked the page is responsive and everything stacks on top on one another at widths below 768px.
**Order confirmation:**
1.	Checked confirmation page loads as it should. 
    * A note to say where the confirmation has been sent appears.
    * A success toast appears confirming the order.
    * All information on the confirmation is relevant and correct:
        * Order info (order number and order date) is shown.
        * Billing info (address and contact number) is shown.
        * Order details shown.
2.	Checked that Stripe has taken the payment.
3.	Checked the order now appears in the database.
4.	Checked that if I’m a registered user the order appears in my profile under order history.
5.	Checked if my delivery information gets saved.
    * If box is ticked then existing information is overwritten.
    * If it’s left unticked then nothing gets saved.
6.	Checked that the page is responsive and everything stacks on top on one another at widths below 768px.
**Profile:**
1.	Checked the page is only accessible to registered users.
2.	Checked that the user’s username appears in the title.
3.	Seen that the page is split into two sections:
    * Saved delivery information form.
        * Form is made up of seven input fields: phone, address 1&2, town or city, county, postcode and country. None of these are required.
        * Checked that if the user has default billing information already saved to their account then the form should be pre-populated with this. 
        * Clicked the update info button to test it submits the form.
            * A toast appears confirming this information has been saved.
    * Order history.
        * Checked that the details of all previous orders made by that user are shown.
            * Date and time of order is shown.
            * Order number is displayed.
            * Order total is shown.
        * The order number acts as a link to the order’s confirmation page.
            * When clicked the order confirmation page loads and all details are correct and present.
            * A toast message appears to say this was a past order.
            * Tested the back to profile button works.
4.	Checked that the page is responsive and everything stacks on top on one another at widths below 768px.
**Music Library:**
1. Checked the page is only accessible to registered users.
2. Checked that all the songs download from soundcloud.
3. Checked all songs

**Add product:**
1.	Checked that the form is accessible by admin only.
2.	Checked that the form is accessible via the link in the navigation bar (admin only).
3.	Checked the number of fields, 8 in total: name, description, price, subscription, access, original music rating and image. Checked all have a relevant label.
4.	Tested the buttons:
    * Pressed products, this takes me to the Bottle Shop.
    * Pressed the choose image button and it does as it should.
    * Pressed add product to try and send an empty form. Input required error message appears.
5.	Tested that the form validated the inputted data correctly. The form will then only send if all fields marked with a * are filled in.
    * Checked that only numbers can be entered into the ABV, size and price fields.
6.  On successful submission of the form I get redirected to the newly created products detail page.
    * A toast appears confirming that the product has been added.
7.	Checked that the product now appears in the database.
8.	Checked that the item now appears throughout the site.
**Edit product:**
1.	Checked that the form is accessible by admin only.
2.	Checked that the form is accessible via the edit button on the service detail page (admin only).
3.	Toast message confirms that you’re now editing the product.
4.	The form is the same as the one that’s found on the add product page but all fields are pre-populated with the existing data.
5.	Tested the buttons:
    * Pressed the choose image button and it does as it should.
    * Pressed update service, the updated service loads and a success toast confirms the update.
6.	Tested that the form still validated the inputted data correctly. The form will then only send if all fields that are required are filled in.
7.	On successful completion of the form I get redirected to the service in questions page, which shows the updated information.
**Delete functions:**
* Deleting a service:
    * Checked that the function can be performed by admin only.
    * When a service is deleted I’m redirected back to the Services page.
    * A toast message appears confirming the deletion.
    * Checked that it can no longer be found on the site.
    * Checked that it can no longer be found in the database.
## Responsiveness
Whilst building my site I have been checking my progress and testing any changes made using Chrome DevTools at different breakpoints. I’ve pretty much solely relied on DevTools as I didn’t deploy my site until later on in the project.
I have physically tested my site on my huawei p30 pro. I have tested for responsiveness on other devices using DevTools alongside the Responsive Design Mode on Firefox. Using these tools I have tested on numerous mobile devices such as the Moto G4, Galaxy S5 and the iPhone range as well as numerous tablet devices in both landscape and portrait views.
## Browser compatibility
I have physically tested my website on the following browsers and devices:
* Chrome (desktop and mobile).
* Firefox (desktop).
* Microsoft Edge (desktop).
* Safari (mobile).
## User Stories
### As a shopper I'd like to:
**"View a selection of services and select those I wish to purchase."**
* The services page is accessible to all users, registered or not.
* Links to view services can be found in the navigation bar, which can be seen at all times.
* There are a number of call-to-action buttons placed throughout the site directing the user to this page.
* Registered users are able to add a service to their cart by clicking on the image.
**"Look at individual service details in order to consolidate my decision on whether to subscribe or not."**
* Every service has its own page that gives further information on the product. The pages are accessed via the products card, which are seen on the services page. The image is the link.
* Further information gets displayed via a table, which breaks the information up. Not only is this a more aesthetically pleasing way to show the information but the table is also responsive at all breakpoints. This means information is always displayed in a clear and informative manner in keeping with the overall style of the site.
* Product name, description, price, subscription type, library access, original music and rating are all shown.
* The service can also be added to the cart from here as the add button is shown.
**"Add items to the cart to purchase at a later point."**
* Users can add an item to their cart by going to the service details page.
    * The add to cart button is displayed here.
**"Easily view the carts contents and the number of items within it."**
* The cart icon found in the navigation bar acts as a direct link to the cart page and as mentioned before the navigation bar is fixed so this link is always visible.
* If the cart has items within it then a total price is displayed.
* When on the cart page the page is titled Shopping Cart.
* Whenever a product is added a toast message appears not only confirming the addition but also gives a summary of what’s currently in the cart.
    * The checkout link at the bottom of the toast will send the user to the carts page.
**"Be given the ability to remove items completely."**
* The only place to remove an item is on the cart page, which as touched on above is easy to get to due to the link in the fixed navigation bar.
    * A toast message appears confirming this alteration.
**"Checkout, pay and complete my order easily."**
* On the checkout page the order is summarised so that the user is shown what they are ordering.
    * In cases of a user forgetting something or they have second thoughts about an item then a button to adjust cart is conveniently placed under this summary and links back to the cart.
    * There is also a note at the bottom of the page (under the place order button) that confirms the order total.
* Adding personal, delivery and payment details is done via a user friendly form.
* Field’s that are required in the form are marked with a * as is the norm.
    * If the form is submitted without one of these fields then the user is informed as tested as part of the manual testing plan.
* On successful completion of the order the user is directed to their order confirmation page.
**"Have order confirmation once my order has been completed."**
* On successful completion of an order the user is automatically directed to the order success page. This page confirms and shows all the information that the user has just inputted as part of the order.
    * A success toast message also appears confirming successful completion of the order.
* On top of this an email confirmation is sent out to the email address provided.
**"Navigate around the site easily and the site to be user friendly."**
* I've used a fixed navigation bar so that links are available at the top of every page and at any point.
* This is also the case on smaller devices but the links get placed into a dropdown menu, which is operational by toggling the hamburger icon / button.
* I’ve placed call-to-action buttons all over the site (where relevant). These are clear in what they do, have hover classes to show they can be interacted with and aid with the overall navigation around the site.
**"Receive feedback whilst interacting with the site."**
* Toast messages appear in the top right of the screen when information needs to be relayed to the user such as when a function has been performed or something has gone wrong i.e. access being denied. 
* Validation messages appear on forms fields when input is invalid or incorrect.
**"Do all of the above regardless of what device I’m using."**
* I have done thorough browser compatibility testing as well as responsiveness testing at different breakpoints. I am confident that the site is suitable for use on a wide range of devices and browsers.
### As a returning user I'd like:
**"To sign up and register for an account easily."**
* The link to register can be found in the navigation bar by clicking the profile link / icon and selecting it from the dropdown menu and on the home page if the user is not reistered.
* Each input field is clearly labelled.
* Registering is as simple as inputting an email address, username and password.
    * For security the password and email address will need to be re-typed.
* A user is clearly informed if the username is in use or if the passwords don’t match.
* All registrations will require email verification to confirm the user is who they say they are.
    * An email asking the user to verify themselves via a link is sent to the email address provided.
**"To receive email confirmation of registration and have the ability to recover forgotten passwords."**
* Email confirmations are sent to verify and confirm registration to The On Call Musician as mentioned above.
* As I’ve used Django allauth to handle user registration, logging in, logging out and verifying accounts etc it also handles other account functionality such as resetting lost passwords.
* When the forgot password link is clicked the user is asked to enter an email address and if it matches one that’s associated with a user in the database then they are sent a reset link to create a new password.
    * Django allauth handles all this really well and in a very user friendly manner.
**"To login and logout easily."**
* The link to login can be found in the navigation bar.
* The logging in process is just as simple as registering with only a username or email address being required along with a password.
    * Each input field is clearly labelled.
    * When successfully logged in a success toast will appear welcoming the user.
* A user is clearly informed if the details provided don’t match.
* To log out the logout link needs to be clicked. This can be found in the navigation bar as well.

**"A personalised user profile where I can see my order history and set my default delivery information if desired."**
* The link that a user can use to access their profile can be found in the navigation bar by clicking the profile link / icon and selecting it from the dropdown menu. This page is only accessible to them and only when they’re signed in.
* The page is personalised and shows past orders.
* A list of all previous orders made by that user is shown. The list gives information such as the date the order was made, its order number and the order total in a clear manner.
    * The order number here also acts as a link to the order confirmation that would have been generated at the time relaying delivery, order and billing details.
    * To stop confusion a toast message appears telling the user that this was a past order.
* Saved billing information can be inputted or is shown via a form on the page.
    * Any information inputted and updated here overrides the users default billing information where it is used in instances such as when checking out.
    * The information shown here can get overridden as part of the checkout process if the user selects to save their information via the checkbox.
**"Access to a music when registered."**
* when a user has registered, they will have access to a library of music.  The link will appear in the navbar.
### As the site owner / admin I want:
**"The ability to add new services to the store."**
* Adding either a new service is done via a form.
* The links to access the form is shown in the navigation bar by clicking the profile link / icon and selecting it from the dropdown menu.
    * These link is only visible to admin.
* Each input field is clearly labelled and includes a placeholder. If the validation requirements aren’t met then the user is informed of this on submission.
* On successful completion we get sent to the newly created page and the product/article can be viewed on the site.
**"To be able to edit and remove products from the store."**
* As with adding services, editing and removing them can only be done by admin with access to the relevant form and functionality restricted.
* To access the edit and delete function of a product, admin needs to navigate to the service page and the relevant link will be shown.
* Editing will take you to the relevant form, which will be pre-populated with the data that’s already been inputted.
    * Form fields are clearly labelled and all data entered is validated the same as when it’s intially added.
* Deleting anything from the site is as simple as clicking the delete link in the services page.
    * Any deletion or update is confirmed by a toast message.
