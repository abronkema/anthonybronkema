const headerIconCode = document.getElementById('code');
const headerIconEmail = document.getElementById('mail');
const headerIconTwitter = document.getElementById('twitter');
const headerIcon = document.querySelector('.header-icons');
const headerNamePrimary = document.querySelector('.header-name__primary');
const headerNameAlt = document.querySelector('.header-name__alt');
let headerNameAltText = headerNameAlt.innerHTML;
const github = "github/anthonybronkema";
const mail = "email me";
const twitter = "twitter/anthonybronkema"

// TODO: Refactor the follow into a non-repeatable function
// TODO: headerNameAltText update should trigger when the background color appears. 

headerIconCode.addEventListener('mouseenter', function(e) {
    headerNamePrimary.classList.toggle('hide');
    headerNameAlt.innerHTML = github;
})
headerIconEmail.addEventListener('mouseenter', function(e) {
    headerNamePrimary.classList.toggle('hide');
    headerNameAlt.innerHTML = mail;
})
headerIconTwitter.addEventListener('mouseenter', function(e) {
    headerNamePrimary.classList.toggle('hide');
    headerNameAlt.innerHTML = twitter;
})

headerIconCode.addEventListener('mouseleave', function() {
    headerNamePrimary.classList.toggle('hide');
    headerNameAlt.innerHTML = "";
})
headerIconEmail.addEventListener('mouseleave', function() {
    headerNamePrimary.classList.toggle('hide');
    headerNameAlt.innerHTML = "";
})
headerIconTwitter.addEventListener('mouseleave', function() {
    headerNamePrimary.classList.toggle('hide');
    headerNameAlt.innerHTML = "";
})

