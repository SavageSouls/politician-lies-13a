/** POST /api/lies */
export default async function handler(req, res) {
    const method = req.method
    if (method=='POST') {
        const body = req.body
        console.log('body', body)
        return res.status(201).json({ok: true})
    } else{
        return res.status(405).json({ok: false})
    }
}