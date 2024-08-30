CREATE TABLE "Asset" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" VARCHAR(200) NOT NULL,
    "reg" VARCHAR(10) NOT NULL
);

CREATE TABLE "Status" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "vehicle_id" INTEGER UNIQUE NOT NULL REFERENCES "Asset" ("id") ON DELETE CASCADE,
    "status" VARCHAR(10) NOT NULL CHECK ("status" IN ('Active', 'Yard', 'Garage'))
);

CREATE INDEX "Status_vehicle_id_idx" ON "Status" ("vehicle_id");
CREATE INDEX "Status_status_idx" ON "Status" ("status");
CREATE INDEX "Status_status_vehicle_id_idx" ON "Status" ("status", "vehicle_id");
