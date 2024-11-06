function initialize() {
  // Click event to change language to English
  $('#change_lang_en').click(() => {
    setLanguageCookieAndReload("en");
  });

  // Click event to change language to Arabic
  $('#change_lang_ar').click(() => {
    setLanguageCookieAndReload("ar");
  });

  // Set the language preference and hide buttons accordingly
  setLanguagePreferences();
}

// Function to set language cookie and reload the page
function setLanguageCookieAndReload(language) {
  document.cookie = `preferred_language=${language}`;
  window.location.reload();
}

// Function to set language preferences
function setLanguagePreferences() {
  let preferred_language = frappe.get_cookie("preferred_language");

  if (preferred_language === "ar") {
    $(".language-switcher-image").attr("src", "/assets/dox_theme/images/ar.png");
    $('#change_lang_ar').hide();
  } else {
    $(".language-switcher-image").attr("src", "/assets/dox_theme/images/en.png");
    $('#change_lang_en').hide();
  }

  // If no preferred language is set, default to Arabic
  if (!preferred_language) {
    document.cookie = `preferred_language=ar`;
    window.location.reload();
  }
}

$(window).ready(initialize);
