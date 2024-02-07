
interface PageParams {
    slug: string;
}




export default async function Page({params}: {params: PageParams}) {
    const slug = params.slug;

    return (
        <main className="flex min-h-screen flex-col items-center justify-between p-24">

            <div>
                <h1>Project {slug}</h1>
            </div>

        </main>
    )
}