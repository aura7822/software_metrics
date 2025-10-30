package java_WITH_selenium;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
public class Java_WITH_selenium{
    public static void main(String[]args){
        System.setProperty("webdriver.gecko.driver","/home/aura/selenium-drivers/geckodrivers");
        WebDriver driver = new FirefoxDriver();
        driver.get("https://elearning.zetech.ac.ke/my/");
        
        System.out.println("Page Title : "+driver.getTitle());
        driver.quit();
    }
}