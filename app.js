const headerNamePrimary = document.querySelector('.header-name__primary');
const headerNameAlt = document.querySelector('.header-name__alt');
const allIcons = document.querySelectorAll('.icon');

const resetHeaderNamePrimary = function() {
    headerNamePrimary.classList.toggle('hide');
    headerNameAlt.innerHTML = "";
}

const setAlternateText = function(event) {
    if (event.target.id === "code") {
        headerNameAlt.innerHTML = "github/anthonybronkema";
    }
    if (event.target.id === "mail") {
        headerNameAlt.innerHTML = "send your feedback";
}
    if (event.target.id === "twitter") {
    headerNameAlt.innerHTML = "twitter/anthonybronkema";
};
};

allIcons.forEach(function(el) {
    if (el.id == "mail") {
        el.addEventListener('click', function(el) {
            console.log(`You clicked ${el.target.id}`);
        })
    }
        el.addEventListener('mouseover', function(event) {
            resetHeaderNamePrimary();
            setAlternateText(event);
        });
        el.addEventListener('mouseleave', function(event) {
            resetHeaderNamePrimary();
        });  
});
