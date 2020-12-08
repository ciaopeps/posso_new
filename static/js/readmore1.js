// Add click event dynamically
$(document).on("click", ".toggle-text-button", function() {

  // Check if text is more or less
  if ($(this).text() == "Read More") {

    // Change link text
    $(this).text("Read Less");
    
    // Travel up DOM tree to parent, then find any children with CLASS .toggle-text and slide down
    $(this).parent().children(".toggle-text").slideDown();
    
  } else {


    // Change link text
    $(this).text("Read More");
    
    // Travel up DOM tree to parent, then find any children with CLASS .toggle-text and slide up 
    $(this).parent().children(".toggle-text").slideUp();
    
  }
  
});