import {Progress} from "@nextui-org/react";


export default function ProjectStorageBar({value}: {value: number | undefined}) {

	if (!value) return null;

	if (value <= 0){
		return (
				<div className="flex flex-col gap-6 w-full max-w-md">
					<Progress color="default" aria-label="Loading..." value={value}/>
				</div>
		)
	} else if (value > 0 && value <= 80){
		return (
				<div className="flex flex-col gap-6 w-full max-w-md">
					<Progress color="default" aria-label="Loading..." value={value}/>
				</div>
		)
	} else if (value > 80 && value <= 90) {
		return (
			<div className="flex flex-col gap-6 w-full max-w-md">
				<Progress color="warning" aria-label="Loading..." value={value}/>
			</div>
		)
	} else {
		return(
			<div className="flex flex-col gap-6 w-full max-w-md">
				<Progress color="danger" aria-label="Loading..." value={value}/>
			</div>
		)
	}
}