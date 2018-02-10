const express = require('express')
const mysql = require('mysql')
const app = express()

const conn = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "12345",
    database: "bookstore"
});

conn.connect((err) => {
    if (err) {
        console.log("Can't connect to db!");
        return
    }
    console.log("connected to db...");
});

app.set('view engine', 'pug')
app.set('views', './views')
app.use(express.json());
app.use('/css', express.static('./css'))
app.use('/js', express.static('./js'))

let dataFields = [];
conn.query('SELECT cate_descrip FROM category', (error, rows) => {
    if (error) throw error;

    rows.forEach((record) => {
        dataFields.push(record.cate_descrip)
    })
})

let allBooks = [];
conn.query(`select author.aut_name, book_name, category.cate_descrip,
 publisher.pub_name, book_price from book_mast join author
  on book_mast.aut_id = author.aut_id join category on category.cate_id
= book_mast.cate_id join publisher on publisher.pub_id = book_mast.pub_id;`, (error, rows) => {
    if (error) throw error;
    allBooks = rows
})

app.get('/filter', (req, res) => {
    let out = 0
    // let status = false
    let filter = ''
    let and1 = ''
    let and2 = ''
    let filterA, filterB, filterC;
    let category = req.query.category
    let lower = req.query.lower
    let higher = req.query.higher
    
    category === '-' 
        ? filterA = '' 
        : (filterA =  `cate_descrip = ${conn.escape(category)}`, filter = 'WHERE', out++)
    lower === '-' 
        ? filterB = '' 
        : (filterB = `book_price < ${conn.escape(Number(lower))}`, filter = 'WHERE', out++)
    higher === '-' 
        ? filterC = '' 
        : (filterC = `book_price > ${conn.escape(Number(higher))}`, filter = 'WHERE', out++)

    if (out === 3) {
        and1 = 'AND', and2 = 'AND'
    }
    if (out === 2) {
        if (filterA === '') {
            and2 = 'AND'
        } else if (filterB === '') {
            and1 = 'AND'
        } else if (filterC === '') {
            and1 = 'AND'
        }
    }

    conn.query(`select author.aut_name, book_name, category.cate_descrip,
    publisher.pub_name, book_price from book_mast join author
     on book_mast.aut_id = author.aut_id join category on category.cate_id
   = book_mast.cate_id join publisher on publisher.pub_id = book_mast.pub_id
    ${filter} ${filterA} ${and1} ${filterB} ${and2} ${filterC}`, (err, rows) => {
        res.status(200)
        res.send(JSON.stringify(rows))
    })
})

app.get('/', (req, res) => {
    res.render('index', { title: 'Bookstore', h1: 'Bookstore!', dataFields: dataFields, allBooks: allBooks })
})

app.listen('8080', () => {
    console.log('server is on the fly...')
})