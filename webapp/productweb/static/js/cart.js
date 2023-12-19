// your_js_file.js
document.addEventListener('DOMContentLoaded', function () {
    var cartInfo = document.getElementById('cart-info');
    var addToCartButtons = document.querySelectorAll('.add-to-cart-btn');
    var cartCount = document.getElementById('cart-count');
    var cartUrl = cartInfo.getAttribute('data-cart-url');  // Access the URL from the data attribute

    addToCartButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            var itemId = this.getAttribute('data-item-id');
            var currentCount = parseInt(cartCount.innerText);
            cartCount.innerText = currentCount + 1;

            // Make an AJAX request to add the item to the cart on the server
            // (You might want to use a library like Fetch or jQuery.ajax for this)
            // Example using Fetch:
            fetch(`/add_to_cart/${itemId}/`)
                .then(response => response.json())
                .then(data => console.log(data))
                .catch(error => console.error('Error:', error));
        });
    });

    cartInfo.addEventListener('click', function () {
        window.location.href = cartUrl;  // Use the cart URL in the JavaScript
    });
});
