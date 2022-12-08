/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Ritesh
 */
public class Model {
    String category,dishname;
   
   
  

   

    Model( String category, String dishname) {
       
       this.dishname=dishname;
       this.category=category;
       
        //throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
   
   
   String getCategory(){
       return category;
       
   }
   String getDishname(){
       return dishname;
   }
  
    
}
