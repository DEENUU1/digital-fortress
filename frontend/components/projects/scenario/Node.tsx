'use client';
import React from "react";
import {Modal, ModalContent, ModalHeader, ModalBody, ModalFooter, Button, useDisclosure} from "@nextui-org/react";

export function ModalResponse({data}: {data: ScenarioResponse}) {
  const {isOpen, onOpen, onOpenChange} = useDisclosure();

  return (
    <>
      <Button onPress={onOpen}>Details</Button>
      <Modal isOpen={isOpen} onOpenChange={onOpenChange} backdrop={"blur"}>
        <ModalContent>
          {(onClose) => (
            <>
              <ModalHeader className="flex flex-col gap-1">Scenario id: {data.id}</ModalHeader>
              <ModalBody>
                <h2 className="text-md font-bold">AI Response</h2>
                <p>{data.response}</p>

                <h2 className="text-md font-bold">User Details</h2>
                <p>{data.user_details}</p>

                <span className="text-gray-500 text-sm">Created: {data.created_at}</span>
                <span className="text-gray-500 text-sm">Updated: {data.updated_at}</span>
              </ModalBody>
              <ModalFooter>
                <Button color="danger" variant="light" onPress={onClose}>
                  Close
                </Button>
              </ModalFooter>
            </>
          )}
        </ModalContent>
      </Modal>
    </>
  );
}


export default function Node({data}: {data: ScenarioResponse}){

  return (
    <div>
      <strong>{data.id}</strong>
      <ModalResponse data={data}></ModalResponse>
    </div>
  );
}