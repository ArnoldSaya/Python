package Clase_Miercoles;

import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.Connection;

public class Principal {
    public static void main(String[] args) {
        try {

            Class.forName("org.sqlite.JDBC");

            Connection con = DriverManager.getConnection("jdbc:sqlite:ejemplo2.db");
            
            if (con != null) {
                System.out.println("Se creó y/o abrió la base de datos: ");
            }
            
            Statement stmt = con.createStatement();
            stmt.execute("CREATE TABLE IF NOT EXISTS Genero (id_genero INTEGER PRIMARY KEY, name_genero TEXT);");
            stmt.execute("CREATE TABLE IF NOT EXISTS Alumnos (id_alumno INTEGER PRIMARY KEY, name TEXT, apellido TEXT, age INTEGER, id_genero INTEGER, FOREIGN KEY (id_genero) REFERENCES Genero(id_genero));");
            
            System.out.println("Creación de tablas exitosa (si no existían)");
            

            //stmt.execute("INSERT INTO Genero (id_genero, name_genero) VALUES (1, 'Masculino');");
            //stmt.execute("INSERT INTO Genero (id_genero, name_genero) VALUES (2, 'Femenino');");
  
            //stmt.execute("INSERT INTO Alumnos (id_alumno, name, apellido, age, id_genero) VALUES (1, 'Carlos', 'Aguilar', 14, 1);");
            //stmt.execute("INSERT INTO Alumnos (id_alumno, name, apellido, age, id_genero) VALUES (2, 'Bety', 'Mendes', 22, 2);");
            //stmt.execute("INSERT INTO Alumnos (id_alumno, name, apellido, age, id_genero) VALUES (3, 'Carlos','Maune', 1, 1);");
            //stmt.execute("INSERT INTO Alumnos (id_alumno, name, apellido, age, id_genero) VALUES (4, 'Bety', 'Letra', 23, 2);");
            //stmt.execute("INSERT INTO Alumnos (id_alumno, name, apellido, age, id_genero) VALUES (5, 'Carlos', 'Lote', 15, 1);");
            //stmt.execute("INSERT INTO Alumnos (id_alumno, name, apellido, age, id_genero) VALUES (6, 'Bety', 'Llora', 54, 2);");
            //stmt.execute("INSERT INTO Alumnos (id_alumno, name, apellido, age, id_genero) VALUES (9, 'Bety', 'Llora', 54, 2);");
            
            
            System.out.println("Inserciones exitosas");

            ResultSet rs = stmt.executeQuery("SELECT * FROM Alumnos");
            while (rs.next()) {
                System.out.println("ID: " + rs.getInt(1) + " " 
            + "Nombre: "+ rs.getString(2) + " " + "Apellido: " + rs.getString(3) + " " + "Edad: " + rs.getInt(4) + " " + "Genero ID:" + rs.getInt(5));
            }

 
            con.close();
            
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
