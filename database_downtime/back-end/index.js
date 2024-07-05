const { Client } = require('pg');
const cors = require('cors');
const express = require('express');

const app = express();

app.use(cors());

app.get('/', async (req, res) => {
  // Replace with your PostgreSQL connection details
  const config = {
    user: 'your-username',
    host: 'your-host',
    database: 'database-name',
    password: 'database-password',
    port: port-number, 
  };

  const client = new Client(config);

  async function checkDatabaseStatus() {
    const startTime = Date.now();

    try {
      await client.connect();
      res.status(200).json({
        statusCode: 200,
        message: "Your connection is up with the database",
      });
    } catch (error) {
      res.status(500).json({
        statusCode: 500,
        message: `Error checking database status: ${error.message}`,
      });
    } finally {
      await client.end();
    }
  }

  await checkDatabaseStatus();
});

const PORT = 3000;
app.listen(PORT, () => console.log(`Server is running on port ${PORT}`));
