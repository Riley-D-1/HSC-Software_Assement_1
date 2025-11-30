function check(){
    // This firstly checks that the email contains a .com and an @ symbol
    // It also checks that the password includes by using the exisitng password testing function
    // The operand && will return true only if all values are true
    let name_ = document.getElementById("name_").value
    // Debugging statement
    console.log("All valid values")
    alert("redirect")
    // Saves the infomation to local storage to display back to user.
    //alert(name)
    localStorage.setItem("Name",name_)

    // You redirect here
    window.location.href = "results.html"
}