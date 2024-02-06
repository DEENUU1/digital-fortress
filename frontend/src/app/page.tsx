'use client';

import { signIn, signOut, useSession } from "next-auth/react";

export default function Home() {
  const { data: session } = useSession();
  console.log({ session });


  return (
      <main className="flex min-h-screen flex-col items-center justify-between p-24">

      </main>
  );
}
