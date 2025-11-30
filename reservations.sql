CREATE TABLE RestaurantReservations(Reservation INTEGER PRIMARY KEY AUTOINCREMENT,
                                    UserName TEXT NOT NULL,
                                    UserEmail TEXT NOT NULL,
                                    ReservationDate TEXT NOT NULL,
                                    Time TEXT NOT NULL,
                                    NumberOfGuests INTEGER NOT NULL);
INSERT INTO RestaurantReservations(UserName,UserEmail,ReservationDate,Time,NumberOfGuests) VALUES
                                ('Alice','alice@example.com','2024-09-20','19:00', 4)
                                ('Bob','bob@example.com','2024-09-27','20:30', 2)
                                ('Charlie','charlie@example.com','2024-09-13','18:45', 3)
                                ('Diana','diana@example.com','2024-09-06','19:30', 5)
                                ('Ethan','ethan@example.com','2024-09-13','21:00', 2);
                    
SELECT * FROM RestaurantReservations 
    Like '%19', '%18'