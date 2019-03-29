const headerNamePrimary = document.querySelector('.header-name__primary');
const headerNameAlt = document.querySelector('.header-name__alt');
const github = "github/anthonybronkema";
const mail = "email me";
const twitter = "twitter/anthonybronkema"
const allIcons = document.querySelectorAll('.icon');

const resetHeaderNamePrimary = function() {
    headerNamePrimary.classList.toggle('hide');
    headerNameAlt.innerHTML = "";
}

const setAlternateText = function(event) {
    if (event.target.id === "code") {
        headerNameAlt.innerHTML = github;
    }
    if (event.target.id === "mail") {
        headerNameAlt.innerHTML = mail;
}
    if (event.target.id === "twitter") {
    headerNameAlt.innerHTML = twitter;
};
};

allIcons.forEach(function(el) {
        el.addEventListener('mouseover', function(event) {
            resetHeaderNamePrimary();
            setAlternateText(event);
        });
        el.addEventListener('mouseleave', function(event) {
            resetHeaderNamePrimary();
        });  
});
