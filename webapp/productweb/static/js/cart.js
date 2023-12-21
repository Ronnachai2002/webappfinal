document.addEventListener('DOMContentLoaded', function () {
    var cartInfo = document.getElementById('cart-info');
    var addToCartButtons = document.querySelectorAll('.add-to-cart-btn');
    var cartCount = document.getElementById('cart-count');
    var cartUrl = cartInfo.getAttribute('data-cart-url');

    addToCartButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            var itemId = this.getAttribute('data-item-id');
            var currentCount = parseInt(cartCount.innerText);

            // Make an AJAX request to add the item to the cart on the server
            fetch(`/add_to_cart/${itemId}/`)
                .then(response => response.json())
                .then(data => {
                    console.log(data); // for debugging
                    // Update the cart count on the page
                    cartCount.innerText = data.total_quantity;
                })
                .catch(error => console.error('Error:', error));
        });
    });

    cartInfo.addEventListener('click', function () {
        window.location.href = cartUrl;
    });
});
