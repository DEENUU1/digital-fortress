import { Handle, Position } from 'reactflow';


export function ChildNode() {

  return (
    <>
      <Handle type="target" position={Position.Top} />
      <div className="bg-black">
        <button className="text-white">Create</button>
        <p className="text-white">Some text here</p>
      </div>
      <Handle type="source" position={Position.Bottom} id="a" />
    </>
  );
}

export function RootNode() {
  return (
    <>
      <div className="bg-black">
        <button className="text-white">Create</button>
      </div>
    </>
  )
}