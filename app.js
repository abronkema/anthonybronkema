const headerNamePrimary = document.querySelector('.header-name__primary');
const headerNameAlt = document.querySelector('.header-name__alt');
const allIcons = document.querySelectorAll('.icon');
const mailIcon = document.querySelector('#mail')

const resetHeaderNamePrimary = function() {
    headerNamePrimary.classList.toggle('hide');
    headerNameAlt.innerHTML = "";
}

function copyTextToClipboard() {
    var emailAddress = 'anthony.bronkema@gmail.com';
    navigator.clipboard.writeText(emailAddress).then(function() {
        // TODO: Make a banner to confirm clipboard copy
        console.log('Clipboard copied!')
    }, function() {
        console.log('Clipboard failed to copy')
    })
}

const setAlternateText = function(event) {
    if (event.target.id === "code") {
        headerNameAlt.innerHTML = "github/abronkema";
    }
    if (event.target.id === "mail") {
        headerNameAlt.innerHTML = "send me a note (copies my email to clipboard)";
        // TODO: remove the note on copying once banner is created.
}
    if (event.target.id === "twitter") {
    headerNameAlt.innerHTML = "twitter/anthonybronkema";
};
};

mailIcon.addEventListener("click", copyTextToClipboard);

allIcons.forEach(function(el) {
    if (el.id == "mail") {
        el.addEventListener('click', function(el) {
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
